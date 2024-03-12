import { Injectable } from '@angular/core';
import {Account} from "./account.service";
import {Timestamp} from "rxjs";

export interface AccountUser {
  id: number
  account: number
  partition: number
  name: string

  password: string

  in_out_codes: string

  phone_number1: string
  phone_number2: string
  phone_number3: string

  title: string

  holiday_begins: Date
  holiday_ends: Date

  keypad_code: string

  hot_user: boolean

  authorized_days_sat: boolean
  authorized_days_sun: boolean
  authorized_days_mon: boolean
  authorized_days_tue: boolean
  authorized_days_wed: boolean
  authorized_days_thu: boolean
  authorized_days_fri: boolean

  created_at: Date
  updated_at: Date
  created_by: number
}

export interface AccountResponse {
  count: number
  results: AccountUser[]
}

@Injectable({
  providedIn: 'root'
})
export class AccountUserService {

  constructor() { }
}
