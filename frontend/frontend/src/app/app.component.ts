import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [RouterModule, SidebarComponent, NgIf],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'frontend'; // 🔹 Agrega esta línea
  constructor(private router: Router) {}

  isLoginPage(): boolean {
    return this.router.url === '/login';
  }

  isSidebarVisible(): boolean {
    return (
      this.router.url.startsWith('/admin') ||
      this.router.url.startsWith('/mesero') ||
      this.router.url.startsWith('/cocinero')
    );
  }
}
