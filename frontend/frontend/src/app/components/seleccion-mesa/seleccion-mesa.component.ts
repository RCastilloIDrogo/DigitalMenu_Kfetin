import { Component, OnInit } from '@angular/core';
import { MesaService } from '../../services/rest/mesa.service';
import { Router } from '@angular/router';
import { CommonModule, NgFor } from '@angular/common';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-seleccion-mesa',
  standalone: true,
  templateUrl: './seleccion-mesa.component.html',
  styleUrls: ['./seleccion-mesa.component.css'],
  imports: [NgFor, CommonModule],
})
export class SeleccionMesaComponent implements OnInit {
  mesas: { id: number; numero: number; estado: string }[] = [];

  constructor(private mesaService: MesaService, private router: Router) {}

  ngOnInit(): void {
    this.mesaService
      .getMesasDisponibles()
      .pipe(
        catchError((error) => {
          console.error('Error obteniendo mesas:', error);
          return of([]);
        })
      )
      .subscribe((data) => {
        this.mesas = data;
        console.log('Mesas recibidas:', this.mesas);
      });
  }

  seleccionarMesa(mesaId: number): void {
    console.log('Mesa seleccionada:', mesaId);
    localStorage.setItem('mesaSeleccionada', mesaId.toString());
    this.router.navigate(['/menu', mesaId]); // ✅ Redirección corregida
  }
}
