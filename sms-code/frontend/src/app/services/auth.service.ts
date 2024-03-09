import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  // http options used for making API calls
  private httpOptions: any;

  // the actual JWT token
  public token: string = "";

  // the token expiration date
  public token_expires: Date | undefined;

  // the username of the logged in user
  public username: string = "";

  // error messages received from the login attempt
  public errors: any = [];

  constructor(private http: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json' })
    };
  }

  // Uses http.post() to get an auth token from djangorestframework-jwt endpoint
  public login(user: any): Observable<any> {
    return new Observable((observer) => {
      this.http.post('api-token-auth/', JSON.stringify(user), this.httpOptions).subscribe({
        next: (data: any) => {
          this.updateData(data['token']);
          observer.next();
        },
        error: (err: any) => {
          this.errors = err.error;
          observer.error();
        }
      })
    })
  }

  // Refreshes the JWT token, to extend the time the user is logged in
  public refreshToken() {
    this.http.post('api-token-refresh/', JSON.stringify({token: this.token}), this.httpOptions).subscribe({
      next: (data: any) => {
        this.updateData(data['token']);
      },
      error: (err: any) => {
        this.errors = err.error;
      }
    });
  }

  public getToken(): any {
    return localStorage.getItem("auth_token")
  }

  public isAuthenticated(): boolean {
    return localStorage.getItem("auth_token") != null;
  }

  public logout() {
    // this.token = null;
    // this.token_expires = null;
    // this.username = null;
  }

  private updateData(token: any) {
    this.token = token;
    localStorage.setItem('auth_token', token);
    this.errors = [];

    // decode the token to read the username and expiration timestamp
    const token_parts = this.token.split(/\./);
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.token_expires = new Date(token_decoded.exp * 1000);
    this.username = token_decoded.username;
  }

}
