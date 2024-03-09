import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'accounts-management',
    loadChildren: () => import('./accounts-management/accounts-management.module').then(m => m.AccountsManagementModule)
  },
  {
    path: 'events-management',
    loadChildren: () => import('./events-management/events-management.module').then(m => m.EventsManagementModule)
  },
  {
    path: 'auth',
    loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule)
  },
  {
    path: '',
    redirectTo: 'auth/login',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
