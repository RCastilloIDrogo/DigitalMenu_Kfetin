import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { MenuDigitalComponent } from './components/menu-digital/menu-digital.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { SeleccionMesaComponent } from './components/seleccion-mesa/seleccion-mesa.component';

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'seleccion-mesa', component: SeleccionMesaComponent },
  { path: 'menu/:id', component: MenuDigitalComponent }, // Manteniendo la selección de mesa

  // Administración
  {
    path: 'admin',
    component: SidebarComponent,
    children: [
      { path: 'usuarios', component: MenuDigitalComponent }, // ⚠️ Luego cambiar por la vista real
      { path: 'mesas', component: MenuDigitalComponent },
      { path: 'menu', component: MenuDigitalComponent },
      { path: 'reportes', component: MenuDigitalComponent },
    ],
  },

  // Mesero
  {
    path: 'mesero',
    component: SidebarComponent,
    children: [
      { path: 'pedidos', component: MenuDigitalComponent },
      { path: 'estado-pedidos', component: MenuDigitalComponent },
    ],
  },

  // Cocinero
  {
    path: 'cocinero',
    component: SidebarComponent,
    children: [
      { path: 'pedidos', component: MenuDigitalComponent },
      { path: 'listos', component: MenuDigitalComponent },
    ],
  },
];
