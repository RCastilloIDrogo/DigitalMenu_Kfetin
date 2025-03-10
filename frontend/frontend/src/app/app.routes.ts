import { Routes } from '@angular/router';
import { SeleccionMesaComponent } from './components/seleccion-mesa/seleccion-mesa.component';
import { MenuDigitalComponent } from './components/menu-digital/menu-digital.component';

export const routes: Routes = [
  { path: '', redirectTo: 'seleccion-mesa', pathMatch: 'full' }, // Página de inicio
  { path: 'seleccion-mesa', component: SeleccionMesaComponent },
  { path: 'menu/:id', component: MenuDigitalComponent }, // Se añade ':id' para pasar la mesa seleccionada
];
