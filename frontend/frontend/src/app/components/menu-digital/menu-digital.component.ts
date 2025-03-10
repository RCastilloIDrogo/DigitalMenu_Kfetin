import { Component, OnInit } from '@angular/core';
import { MenuService } from '../../services/menu.service';
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
  platos: any[] = [];
  carrito: any[] = [];
  errorMessage: string = ''; // 🔹 Para mostrar errores en la UI

  constructor(private menuService: MenuService) {}

  ngOnInit(): void {
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
  }

  agregarAlCarrito(plato: any): void {
    const item = this.carrito.find((p) => p.id === plato.id);
    if (item) {
      item.cantidad++;
    } else {
      this.carrito.push({ ...plato, cantidad: 1 });
    }
  }

  eliminarDelCarrito(plato: any): void {
    this.carrito = this.carrito.filter((p) => p.id !== plato.id);
  }
}
