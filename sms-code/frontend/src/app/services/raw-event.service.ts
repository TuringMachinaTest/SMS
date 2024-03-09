import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from "@angular/common/http";
import {AuthService} from "./auth.service";
import {Observable} from "rxjs";

export interface RawEvent {
  id: number
  data: string
  device_name: string
  created_at: Date
}

export interface RawEventResponse {
  count: number
  results: RawEvent[]
}

@Injectable({
  providedIn: 'root'
})
export class RawEventService {

  private url = "v1/events_management/raw_events/"
  headers = { 'content-type': 'application/json',  'Authorization': 'JWT ' + this._authService.getToken()}

  constructor(private httpClient: HttpClient, private _authService: AuthService) { }

  getAll$(page: number, limit: number = -1, offset: number = -1): Observable<RawEventResponse> {

    const options = {
      params: new HttpParams()
      .set('page', page),
      headers: this.headers,
    }
      limit == -1 ? options.params.set('limit', limit) :""
      limit == -1 ? options.params.set('offset', offset) : ""


    return this.httpClient.get<RawEventResponse>(this.url, options);
  }

}
