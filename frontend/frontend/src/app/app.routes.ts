import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { GestionUsuariosComponent } from './components/admin/gestion-usuarios/gestion-usuarios.component';
import { GestionMesasComponent } from './components/admin/gestion-mesas/gestion-mesas.component';
import { GestionMenuComponent } from './components/admin/gestion-menu/gestion-menu.component';
import { ReportesComponent } from './components/admin/reportes/reportes.component';
import { SeleccionMesaComponent } from './components/seleccion-mesa/seleccion-mesa.component';
import { MenuDigitalComponent } from './components/menu-digital/menu-digital.component';
import { AdminComponent } from './components/admin/admin/admin.component';
export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'seleccion-mesa', component: SeleccionMesaComponent },
  { path: 'menu/:id', component: MenuDigitalComponent },

  // 🔹 Administración (Usamos `AdminComponent`, NO `SidebarComponent`)
  {
    path: 'admin',
    component: AdminComponent,
    children: [
      { path: 'gestionusuarios', component: GestionUsuariosComponent },
      { path: 'gestionmesas', component: GestionMesasComponent },
      { path: 'gestionmenu', component: GestionMenuComponent },
      { path: 'reportes', component: ReportesComponent },
      { path: '', redirectTo: 'gestionusuarios', pathMatch: 'full' }, // Redirección por defecto
    ],
  },

  { path: '**', redirectTo: 'login', pathMatch: 'full' }, // Redirección a login si la ruta no existe
];
