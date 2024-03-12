import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {AuthService} from "./auth.service";

export interface City {
  id: number;
  name: string;
}

export interface CityResponse {
  count: number;
  results: City[];
}

@Injectable({
  providedIn: 'root'
})
export class CityService {

  private url = "v1/accounts_management/cities/"
  headers = { 'content-type': 'application/json',  'Authorization': 'JWT ' + this._authService.getToken()}

  constructor(private httpClient: HttpClient, private _authService: AuthService) { }

  getAll$(page: number, limit: number = -1, offset: number = -1): Observable<CityResponse> {

    const options = {
      params: new HttpParams()
      .set('page', page),
      headers: this.headers,
    }
      limit == -1 ? options.params.set('limit', limit) :""
      limit == -1 ? options.params.set('offset', offset) : ""


    return this.httpClient.get<CityResponse>(this.url, options);
  }

   get$(account:City): Observable<City> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    return this.httpClient.get<City>(this.url + account.id + "/", options)
  }


  add$(account:City): Observable<City> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    const body = JSON.stringify(account);

    return this.httpClient.post<City>(this.url, account, options)
  }

  edit$(account:City): Observable<City> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    const body = JSON.stringify(account);

    return this.httpClient.put<City>(this.url + account.id + "/" , body, options)
  }

  delete$(account:City): Observable<any> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    return this.httpClient.delete<any>(this.url + account.id + "/" , options)
  }


}
