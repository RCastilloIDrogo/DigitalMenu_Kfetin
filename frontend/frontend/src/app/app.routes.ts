import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { SeleccionMesaComponent } from './components/seleccion-mesa/seleccion-mesa.component';
import { MenuDigitalComponent } from './components/menu-digital/menu-digital.component';

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' }, // Página de inicio redirige al login
  { path: 'login', component: LoginComponent },
  { path: 'seleccion-mesa', component: SeleccionMesaComponent }, // Mantengo esta ruta
  { path: 'menu/:id', component: MenuDigitalComponent },
  { path: 'admin', component: MenuDigitalComponent },
  { path: 'mesero', component: MenuDigitalComponent },
  { path: 'cocinero', component: MenuDigitalComponent },
];
