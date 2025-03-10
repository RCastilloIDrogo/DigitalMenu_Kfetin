import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class MesaService {
  private apiUrl = 'http://127.0.0.1:8000/api/mesas/';

  constructor(private http: HttpClient) {}

  getMesasDisponibles(): Observable<any[]> {
    // 🔹 Asegurar que este método exista
    return this.http.get<any[]>(this.apiUrl);
  }
}
