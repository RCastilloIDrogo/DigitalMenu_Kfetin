import { Component } from '@angular/core';
import { SidebarComponent } from '../../sidebar/sidebar.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-gestion-menu',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './gestion-menu.component.html',
  styleUrl: './gestion-menu.component.css',
})
export class GestionMenuComponent {}
