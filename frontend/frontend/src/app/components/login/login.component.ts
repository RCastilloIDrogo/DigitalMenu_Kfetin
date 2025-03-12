import { Component } from '@angular/core';
import { AuthService } from '../../services/auth/auth.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [FormsModule, CommonModule],
})
export class LoginComponent {
  username = '';
  password = '';
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  login(): void {
    this.authService
      .login({ username: this.username, password: this.password })
      .subscribe(
        (response) => {
          localStorage.setItem('token', response.access);
          localStorage.setItem('role', response.role); // Guardamos el rol del usuario

          alert('Login exitoso!');
          this.redirectUser(response.role);
        },
        (error) => {
          this.errorMessage = 'Credenciales incorrectas.';
        }
      );
  }

  redirectUser(role: string): void {
    if (role === 'admin') {
      this.router.navigate(['/admin']);
    } else if (role === 'mesero') {
      this.router.navigate(['/mesero']);
    } else if (role === 'cocinero') {
      this.router.navigate(['/cocinero']);
    } else {
      this.router.navigate(['/menu']);
    }
  }
}
