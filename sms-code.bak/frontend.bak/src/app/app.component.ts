import { Component, OnInit } from '@angular/core';
import { AuthService } from './services/auth.service';
import { NbSidebarService } from '@nebular/theme';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  isAuthenticated = false;

  constructor(private authService: AuthService, private sidebarService: NbSidebarService) {}

  ngOnInit() {
    this.authService.refreshToken();
    this.isAuthenticated = this.authService.isAuthenticated();
  }

  logout() {
    this.authService.logout();
    window.location.href = '/';
  }

}
