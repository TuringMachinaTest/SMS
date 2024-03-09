import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string = ""
  password: string = ""
  message: string = ""

  constructor(private authService: AuthService) { }

  ngOnInit() {
    // if authenticated reload to dashboard url
    if (this.authService.isAuthenticated()) {
      window.location.href = '/dashboard'
    }
  }

  login() {
    this.authService.login({username: this.username, password: this.password})
      .subscribe({
        next: data => {
          console.log(data)
          this.message = 'Login successful!'
          // reload to dashboard url
          window.location.href = '/dashboard'
        },
        error: error => {
          console.log(error)
          this.message = 'Invalid email or password.'
        }
      })
  }

}
