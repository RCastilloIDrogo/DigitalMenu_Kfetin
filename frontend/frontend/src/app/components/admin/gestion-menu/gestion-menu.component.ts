import { Component, OnInit } from '@angular/core';
import { MenuService } from '../../../services/rest/menu.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-gestion-menu',
  standalone: true,
  templateUrl: './gestion-menu.component.html',
  styleUrls: ['./gestion-menu.component.css'],
  imports: [CommonModule, FormsModule],
})
export class GestionMenuComponent implements OnInit {
  platos: any[] = [];
  platoFormulario = {
    nombre: '',
    categoria: '',
    precio_personal: '',
    precio_mediana: '',
    precio_grande: '',
  };
  platoEditando: any = null;
  mensajeError = '';

  constructor(private menuService: MenuService) {}

  ngOnInit(): void {
    this.cargarPlatos();
    this.cargarCategorias();
  }

  cargarPlatos(): void {
    this.menuService.getPlatos().subscribe(
      (data) => (this.platos = data),
      (error) => (this.mensajeError = 'Error al cargar los platos.')
    );
  }

  cargarCategorias(): void {
    this.menuService.getCategorias().subscribe(
      (data) => (this.categorias = data),
      (error) => (this.mensajeError = 'Error al cargar categorías.')
    );
  }

  seleccionarPlato(plato: any): void {
    this.platoEditando = { ...plato };
    this.platoFormulario = { ...plato }; // Copiamos los valores para el formulario
  }

  agregarPlato(): void {
    this.menuService.crearPlato(this.platoFormulario).subscribe(
      () => {
        this.cargarPlatos();
        this.resetFormulario();
      },
      (error) => (this.mensajeError = 'Error al agregar el plato.')
    );
  }

  editarPlato(): void {
    if (!this.platoEditando) return;

    this.menuService
      .actualizarPlato(this.platoEditando.id, this.platoFormulario)
      .subscribe(
        () => {
          this.cargarPlatos();
          this.resetFormulario();
        },
        (error) => (this.mensajeError = 'Error al actualizar el plato.')
      );
  }

  eliminarPlato(id: number): void {
    if (confirm('¿Estás seguro de eliminar este plato?')) {
      this.menuService.eliminarPlato(id).subscribe(() => {
        this.cargarPlatos();
      });
    }
  }

  resetFormulario(): void {
    this.platoEditando = null;
    this.platoFormulario = {
      nombre: '',
      categoria: '',
      precio_personal: '',
      precio_mediana: '',
      precio_grande: '',
    };
  }
}
