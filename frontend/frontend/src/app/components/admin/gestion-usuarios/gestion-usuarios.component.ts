import { Component, OnInit } from '@angular/core';
import { UsuarioService } from '../../../services/user/usuario.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-gestion-usuarios',
  standalone: true,
  templateUrl: './gestion-usuarios.component.html',
  styleUrls: ['./gestion-usuarios.component.css'],
  imports: [CommonModule, FormsModule],
})
export class GestionUsuariosComponent implements OnInit {
  usuarios: any[] = [];
  nuevoUsuario = { username: '', email: '', role: '' };
  usuarioEditando: any = null;
  mensajeError = '';

  constructor(private usuarioService: UsuarioService) {}

  ngOnInit(): void {
    this.cargarUsuarios();
  }

  cargarUsuarios(): void {
    this.usuarioService.getUsuarios().subscribe(
      (data) => (this.usuarios = data),
      (error) => (this.mensajeError = 'Error al cargar usuarios.')
    );
  }

  agregarUsuario(): void {
    this.usuarioService.crearUsuario(this.nuevoUsuario).subscribe(
      () => {
        this.cargarUsuarios();
        this.nuevoUsuario = { username: '', email: '', role: '' };
      },
      (error) => (this.mensajeError = 'Error al crear usuario.')
    );
  }

  seleccionarUsuario(usuario: any): void {
    this.usuarioEditando = { ...usuario };
  }

  editarUsuario(): void {
    this.usuarioService
      .actualizarUsuario(this.usuarioEditando.id, this.usuarioEditando)
      .subscribe(
        () => {
          this.cargarUsuarios();
          this.usuarioEditando = null;
        },
        (error) => (this.mensajeError = 'Error al actualizar usuario.')
      );
  }

  eliminarUsuario(id: number): void {
    if (confirm('¿Estás seguro de eliminar este usuario?')) {
      this.usuarioService.eliminarUsuario(id).subscribe(() => {
        this.cargarUsuarios();
      });
    }
  }
}
