import { Component, OnInit } from '@angular/core';
import { MesaService } from '../../services/mesa.service';
import { Router } from '@angular/router';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-seleccion-mesa',
  standalone: true,
  imports: [NgFor],
  templateUrl: './seleccion-mesa.component.html',
  styleUrls: ['./seleccion-mesa.component.css'],
})
export class SeleccionMesaComponent implements OnInit {
  mesas: any[] = [];

  constructor(private mesaService: MesaService, private router: Router) {}

  ngOnInit(): void {
    this.mesaService.getMesasDisponibles().subscribe((data) => {
      this.mesas = data;
    });
  }

  seleccionarMesa(mesaId: number): void {
    localStorage.setItem('mesaSeleccionada', mesaId.toString()); // Guardar en localStorage
    this.router.navigate(['/menu']); // Redirigir al menú digital
  }
}
