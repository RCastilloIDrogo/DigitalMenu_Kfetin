import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SidebarComponent } from '../../sidebar/sidebar.component'; // ✅ Importamos el sidebar aquí

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  standalone: true,
  imports: [RouterModule, SidebarComponent], // ✅ Agregamos SidebarComponent aquí
})
export class AdminComponent {}
