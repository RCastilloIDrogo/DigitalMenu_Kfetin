import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class MenuService {
  private apiPlatosUrl = 'http://127.0.0.1:8000/api/menu/platos/'; // ✅ URL para obtener platos
  private apiPedidosUrl = 'http://127.0.0.1:8000/api/pedidos/cliente/'; // ✅ URL correcta para pedidos

  constructor(private http: HttpClient) {}

  getPlatos(): Observable<any[]> {
    return this.http.get<any[]>(this.apiPlatosUrl);
  }

  enviarPedido(pedido: any): Observable<any> {
    return this.http.post<any>(this.apiPedidosUrl, pedido); // ✅ Cambiamos la URL aquí
  }
}
