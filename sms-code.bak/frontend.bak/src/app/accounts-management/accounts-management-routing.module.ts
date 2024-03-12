import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AccountsManagementComponent } from './accounts-management.component';
import { AccountsComponent } from './accounts/accounts.component';
import { CitiesComponent } from './cities/cities.component';

const routes: Routes = [
  {path: "accounts" , component: AccountsComponent},
  {path: "cities" , component: CitiesComponent},
  {path: '', component: AccountsManagementComponent}
]


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AccountsManagementRoutingModule { }
