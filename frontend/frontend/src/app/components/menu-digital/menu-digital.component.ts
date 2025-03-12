import { Component, OnInit } from '@angular/core';
import { MenuService } from '../../services/rest/menu.service';
import { ActivatedRoute } from '@angular/router';
import { NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-menu-digital',
  imports: [NgFor, NgIf],
  standalone: true,
  templateUrl: './menu-digital.component.html',
  styleUrls: ['./menu-digital.component.css'],
})
export class MenuDigitalComponent implements OnInit {
  platos: any[] = [];
  carrito: any[] = [];
  mesaId: string | null = null; // Definir propiedad para la mesa

  constructor(
    private menuService: MenuService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    // Obtener platos del menú
    this.menuService.getPlatos().subscribe((data) => {
      this.platos = data;
    });

    // Obtener el ID de la mesa desde la URL
    this.mesaId = this.route.snapshot.paramMap.get('mesaId');

    // Cargar el carrito desde localStorage
    const carritoGuardado = localStorage.getItem('carrito');
    if (carritoGuardado) {
      this.carrito = JSON.parse(carritoGuardado);
    }
  }

  agregarAlCarrito(plato: any, tamaño: string): void {
    let precioSeleccionado = 0;

    switch (tamaño) {
      case 'personal':
        precioSeleccionado = plato.precio_personal;
        break;
      case 'mediana':
        precioSeleccionado = plato.precio_mediana;
        break;
      case 'grande':
        precioSeleccionado = plato.precio_grande;
        break;
      default:
        alert('Selecciona un tamaño válido.');
        return;
    }

    const item = this.carrito.find(
      (p) => p.id === plato.id && p.tamaño === tamaño
    );
    if (item) {
      item.cantidad++;
    } else {
      this.carrito.push({
        ...plato,
        tamaño,
        precio: precioSeleccionado,
        cantidad: 1,
      });
    }

    localStorage.setItem('carrito', JSON.stringify(this.carrito)); // Guardar en localStorage
  }

  eliminarDelCarrito(plato: any): void {
    this.carrito = this.carrito.filter(
      (p) => !(p.id === plato.id && p.tamaño === plato.tamaño)
    );
    localStorage.setItem('carrito', JSON.stringify(this.carrito));
  }

  confirmarPedido(): void {
    let mesaSeleccionada = localStorage.getItem('mesaSeleccionada');

    if (!mesaSeleccionada) {
      alert('No seleccionaste una mesa. Te asignaremos una automáticamente.');
      mesaSeleccionada = '1'; // 🔹 Asignar la mesa 1 por defecto (puedes cambiarlo)
      localStorage.setItem('mesaSeleccionada', mesaSeleccionada);
    }

    const pedido = {
      mesa: parseInt(mesaSeleccionada, 10),
      detalles: this.carrito.map((item) => ({
        plato: item.id,
        tamaño: item.tamaño,
        cantidad: item.cantidad,
        precio: item.precio,
      })),
    };

    this.menuService.enviarPedido(pedido).subscribe(
      (response) => {
        alert('Pedido enviado con éxito!');
        this.carrito = [];
        localStorage.removeItem('carrito');
      },
      (error) => {
        alert('Error al enviar pedido. Inténtelo nuevamente.');
      }
    );
  }
}
