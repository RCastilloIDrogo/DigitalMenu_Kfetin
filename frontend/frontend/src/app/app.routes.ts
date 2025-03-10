import { Routes } from '@angular/router';
import { MenuDigitalComponent } from './components/menu-digital/menu-digital.component';
import { SeleccionMesaComponent } from './components/seleccion-mesa/seleccion-mesa.component';

export const routes: Routes = [
  { path: '', redirectTo: 'menu', pathMatch: 'full' }, // Redirige a /menu por defecto
  { path: 'menu', component: MenuDigitalComponent }, // Ruta para el menú digital
  { path: 'seleccion-mesa', component: SeleccionMesaComponent }, // Ruta para el menú digital
  { path: '**', redirectTo: 'menu' }, // Cualquier ruta desconocida redirige al menú
];
