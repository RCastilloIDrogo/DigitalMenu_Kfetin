import { Component, OnInit } from '@angular/core';
import { MenuService } from '../../services/menu.service';
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

  constructor(private menuService: MenuService) {}

  ngOnInit(): void {
    this.menuService.getPlatos().subscribe((data) => {
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
