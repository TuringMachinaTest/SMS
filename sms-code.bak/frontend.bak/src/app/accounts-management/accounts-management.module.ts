import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AccountsManagementComponent } from './accounts-management.component';
import { AccountsManagementRoutingModule } from './accounts-management-routing.module';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatSort, MatSortModule} from '@angular/material/sort';
import {MatTableDataSource, MatTableModule} from '@angular/material/table';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { AccountsComponent } from './accounts/accounts.component';
import {MatProgressBarModule} from '@angular/material/progress-bar';
import { MatIcon } from '@angular/material/icon';
import {MatButton, MatIconButton} from '@angular/material/button';
import { MatGridListModule } from '@angular/material/grid-list'
import { AccountComponent } from './account/account.component';

import {
  MatDialog,
  MAT_DIALOG_DATA,
  MatDialogRef,
  MatDialogTitle,
  MatDialogContent,
  MatDialogActions,
  MatDialogClose,
  MatDialogModule
} from '@angular/material/dialog';
import { FormsModule } from '@angular/forms';
import { SharedModule } from '../shared/shared.module';
import { CitiesComponent } from './cities/cities.component';
import { CityComponent } from './city/city.component';
import { MatSelect, MatSelectModule } from '@angular/material/select';
import {MatTabsModule} from '@angular/material/tabs';
import {MatExpansionModule} from "@angular/material/expansion";
import {AccountUsersComponent} from "./account-users/account-users.component";
import {MatListItem, MatListItemMeta, MatListItemTitle, MatListModule, MatNavList} from "@angular/material/list";

@NgModule({
  imports: [
    CommonModule,
    AccountsManagementRoutingModule,

    MatFormFieldModule, MatInputModule, MatTableModule, MatSortModule,
    MatPaginatorModule, MatProgressBarModule, MatIcon, MatButton, MatDialogModule,
    MatFormFieldModule, MatInputModule, MatGridListModule, MatSelectModule, MatTabsModule,
    MatExpansionModule,


    FormsModule,

    SharedModule, MatIconButton, MatListModule

  ],
  declarations: [
    AccountsManagementComponent,
    AccountsComponent, AccountComponent,
    CitiesComponent, CityComponent, AccountUsersComponent]
})
export class AccountsManagementModule { }
