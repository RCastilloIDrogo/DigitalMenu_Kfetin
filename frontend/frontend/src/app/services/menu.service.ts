import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class MenuService {
  private apiUrl = 'http://127.0.0.1:8000/api/menu/platos/'; // URL del backend

  constructor(private http: HttpClient) {}

  getPlatos(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
