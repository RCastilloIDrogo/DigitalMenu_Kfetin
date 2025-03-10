import { Component, OnInit } from '@angular/core';
import { MenuService } from '../../services/menu.service';
import { ActivatedRoute } from '@angular/router';
import { NgFor, NgIf } from '@angular/common';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-menu-digital',
  imports: [NgFor, NgIf],
  standalone: true,
  templateUrl: './menu-digital.component.html',
  styleUrls: ['./menu-digital.component.css'],
})
export class MenuDigitalComponent implements OnInit {
  mesaId: number | null = null;
  platos: any[] = [];
  carrito: any[] = [];
  errorMessage: string = ''; // Para mostrar errores en la UI

  constructor(
    private menuService: MenuService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    // Obtener el ID de la mesa desde la URL
    this.mesaId = Number(this.route.snapshot.paramMap.get('id'));
    console.log('Mesa seleccionada:', this.mesaId);

    // Cargar los platos desde el servicio
    this.menuService
      .getPlatos()
      .pipe(
        catchError((error) => {
          console.error('Error al obtener los platos:', error);
          this.errorMessage =
            'No se pudieron cargar los platos. Inténtalo más tarde.';
          return of([]); // Devolvemos un array vacío para evitar que la app se rompa
        })
      )
      .subscribe((data) => {
        this.platos = data;
      });

    // Recuperar carrito del localStorage si existe
    const carritoGuardado = localStorage.getItem('carrito');
    if (carritoGuardado) {
      this.carrito = JSON.parse(carritoGuardado);
    }
  }

  agregarAlCarrito(plato: any): void {
    const item = this.carrito.find((p) => p.id === plato.id);
    if (item) {
      item.cantidad++;
    } else {
      this.carrito.push({ ...plato, cantidad: 1 });
    }
    this.guardarCarrito();
  }

  eliminarDelCarrito(plato: any): void {
    this.carrito = this.carrito.filter((p) => p.id !== plato.id);
    this.guardarCarrito();
  }

  guardarCarrito(): void {
    localStorage.setItem('carrito', JSON.stringify(this.carrito));
  }
}
