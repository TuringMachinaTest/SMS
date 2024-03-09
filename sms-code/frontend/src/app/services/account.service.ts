import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable, Timestamp} from 'rxjs';
import {AuthService} from "./auth.service";

export interface Account {
  id: number
  number: number
  name: string

  city: number
  city_name: number
  zip_code: string

  address_line1: string
  address_line2: string
  address_line3: string

  email: string
  phone_number1: string
  phone_number2: string
  whatsapp_number: string

  security_number: string

  memo: string

  police_number1: string
  police_number2: string
  police_number3: string

  fire_dept_number1: string
  fire_dept_number2: string
  fire_dept_number3: string

  emergency_number1: string
  emergency_number2: string
  emergency_number3: string

  partition_name1: string
  partition_name2: string
  partition_name3: string
  partition_name4: string
  partition_name5: string
  partition_name6: string
  partition_name7: string
  partition_name8: string
  partition_name9: string
  partition_name10: string

  created_at: Date
  updated_at: Date
  created_by: number
}

export interface AccountResponse {
  count: number
  results: Account[]
}

@Injectable({
  providedIn: 'root'
})
export class AccountService {
  private url = "v1/accounts_management/accounts/"
  headers = { 'content-type': 'application/json', 'Authorization': 'JWT ' + this._authService.getToken()}

  constructor(private httpClient: HttpClient, private _authService: AuthService) { }

  getAll$(page: number, limit: number = -1, offset: number = -1): Observable<Response> {

    const options = {
      params: new HttpParams()
      .set('page', page),
      headers: this.headers,
    }
      limit == -1 ? options.params.set('limit', limit) :""
      limit == -1 ? options.params.set('offset', offset) : ""


    return this.httpClient.get<Response>(this.url, options);
  }

   get$(account:Account): Observable<Account> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    return this.httpClient.get<Account>(this.url + account.id + "/", options)
  }


  add$(account:Account): Observable<Account> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    console.log(account)

    const body = JSON.stringify(account);
    return this.httpClient.post<Account>(this.url, account, options)
  }

  edit$(account:Account): Observable<Account> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    const body = JSON.stringify(account);

    return this.httpClient.put<Account>(this.url + account.id + "/" , body, options)
  }

  delete$(account:Account): Observable<any> {

    const options = {
      params: new HttpParams(),
      headers: this.headers,
    }

    return this.httpClient.delete<any>(this.url + account.id + "/" , options)
  }


}
