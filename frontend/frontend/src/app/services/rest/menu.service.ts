import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class MenuService {
  private apiPlatosUrl = 'http://127.0.0.1:8000/api/menu/platos/';
  private apiPedidosUrl = 'http://127.0.0.1:8000/api/pedidos/cliente/';

  constructor(private http: HttpClient) {}

  private getHeaders(): HttpHeaders {
    const token = localStorage.getItem('token');
    let headers = new HttpHeaders().set('Content-Type', 'application/json');

    if (token) {
      headers = headers.set('Authorization', `Bearer ${token}`);
    }

    return headers;
  }

  // ✅ Obtener todos los platos
  getPlatos(): Observable<any[]> {
    return this.http.get<any[]>(this.apiPlatosUrl, {
      headers: this.getHeaders(),
    });
  }

  // ✅ Crear un nuevo plato
  crearPlato(plato: any): Observable<any> {
    return this.http.post<any>(this.apiPlatosUrl, plato, {
      headers: this.getHeaders(),
    });
  }

  // ✅ Editar un plato
  actualizarPlato(id: number, plato: any): Observable<any> {
    return this.http.put<any>(`${this.apiPlatosUrl}${id}/`, plato, {
      headers: this.getHeaders(),
    });
  }

  // ✅ Eliminar un plato
  eliminarPlato(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiPlatosUrl}${id}/`, {
      headers: this.getHeaders(),
    });
  }

  // ✅ Enviar un pedido
  enviarPedido(pedido: any): Observable<any> {
    return this.http.post<any>(this.apiPedidosUrl, pedido, {
      headers: this.getHeaders(),
    });
  }

  getCategorias(): Observable<any[]> {
    return this.http.get<any[]>('http://127.0.0.1:8000/api/menu/categorias/', {
      headers: this.getHeaders(),
    });
  }
}
