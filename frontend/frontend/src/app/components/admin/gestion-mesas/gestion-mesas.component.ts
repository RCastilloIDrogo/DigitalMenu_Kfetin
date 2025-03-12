import { Component, OnInit } from '@angular/core';
import { MesaService } from '../../../services/rest/mesa.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-gestion-mesas',
  standalone: true,
  templateUrl: './gestion-mesas.component.html',
  styleUrls: ['./gestion-mesas.component.css'],
  imports: [CommonModule, FormsModule],
})
export class GestionMesasComponent implements OnInit {
  mesas: any[] = [];
  nuevaMesa = { numero: '', estado: 'disponible' };
  mensajeError = '';

  constructor(private mesaService: MesaService) {}

  ngOnInit(): void {
    this.cargarMesas();
  }

  cargarMesas(): void {
    this.mesaService.getMesas().subscribe(
      (data) => (this.mesas = data),
      (error) => (this.mensajeError = 'Error al cargar las mesas.')
    );
  }

  agregarMesa(): void {
    if (!this.nuevaMesa.numero) {
      alert('Debe ingresar un número de mesa.');
      return;
    }

    this.mesaService.crearMesa(this.nuevaMesa).subscribe(
      (response) => {
        console.log('Mesa creada correctamente:', response);
        this.cargarMesas(); // Recargar la lista
        this.nuevaMesa = { numero: '', estado: 'disponible' }; // Resetear formulario
      },
      (error) => {
        console.error('Error al crear mesa:', error);
        alert('Error al crear la mesa. Verifica los datos.');
      }
    );
  }

  cambiarEstadoMesa(id: number, estado: string): void {
    const nuevoEstado = estado === 'disponible' ? 'ocupada' : 'disponible';
    this.mesaService.actualizarEstadoMesa(id, nuevoEstado).subscribe(() => {
      this.cargarMesas();
    });
  }

  eliminarMesa(id: number): void {
    if (confirm('¿Estás seguro de eliminar esta mesa?')) {
      this.mesaService.eliminarMesa(id).subscribe(() => {
        this.cargarMesas();
      });
    }
  }
}
