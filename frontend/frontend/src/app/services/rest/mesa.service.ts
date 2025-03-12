import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class MesaService {
  private apiUrl = 'http://127.0.0.1:8000/api/mesas/';

  constructor(private http: HttpClient) {}

  private getHeaders(): HttpHeaders {
    const token = localStorage.getItem('token');

    // Evitar errores si el token no está disponible
    if (!token) {
      console.error('No hay token disponible.');
      return new HttpHeaders({ 'Content-Type': 'application/json' });
    }

    return new HttpHeaders({
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    });
  }

  // ✅ Obtener todas las mesas
  getMesas(): Observable<any[]> {
    return this.http
      .get<any[]>(this.apiUrl, { headers: this.getHeaders() })
      .pipe(catchError(this.handleError));
  }

  // ✅ Obtener solo las mesas disponibles (validar que el backend lo soporte)
  getMesasDisponibles(): Observable<any[]> {
    return this.http
      .get<any[]>(`${this.apiUrl}?estado=disponible`, {
        headers: this.getHeaders(),
      })
      .pipe(catchError(this.handleError));
  }

  // ✅ Crear una nueva mesa (solo admin)
  crearMesa(mesa: any): Observable<any> {
    console.log('Enviando esta mesa:', mesa); // 🔍 Ver qué datos se están enviando

    return this.http
      .post<any>(`${this.apiUrl}crear/`, mesa, {
        headers: this.getHeaders(),
      })
      .pipe(catchError(this.handleError));
  }

  // ✅ Cambiar el estado de la mesa (ocupada/disponible)
  actualizarEstadoMesa(id: number, estado: string): Observable<any> {
    return this.http
      .patch<any>(
        `${this.apiUrl}${id}/estado/`,
        { estado },
        { headers: this.getHeaders() }
      )
      .pipe(catchError(this.handleError));
  }

  // ✅ Eliminar una mesa
  eliminarMesa(id: number): Observable<any> {
    return this.http
      .delete<any>(`${this.apiUrl}${id}/`, {
        headers: this.getHeaders(),
      })
      .pipe(catchError(this.handleError));
  }

  // 🔹 Método genérico para manejar errores en todas las peticiones
  private handleError(error: any): Observable<never> {
    console.error('Error en la API:', error);
    return throwError(() => new Error('Error en la API. Inténtalo de nuevo.'));
  }
}
