import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {EventsManagementRoutingModule} from "./events-management-routing.module";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {MatTableModule} from "@angular/material/table";
import {MatSortModule} from "@angular/material/sort";
import {MatPaginatorModule} from "@angular/material/paginator";
import {MatProgressBarModule} from "@angular/material/progress-bar";
import {MatIcon} from "@angular/material/icon";
import {MatButton, MatIconButton} from "@angular/material/button";
import {MatDialogModule} from "@angular/material/dialog";
import {MatGridListModule} from "@angular/material/grid-list";
import {MatSelectModule} from "@angular/material/select";
import {MatTabsModule} from "@angular/material/tabs";
import {MatExpansionModule} from "@angular/material/expansion";
import {FormsModule} from "@angular/forms";
import {SharedModule} from "../shared/shared.module";
import {MatListModule} from "@angular/material/list";



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    EventsManagementRoutingModule,

    MatFormFieldModule, MatInputModule, MatTableModule, MatSortModule,
    MatPaginatorModule, MatProgressBarModule, MatIcon, MatButton, MatDialogModule,
    MatFormFieldModule, MatInputModule, MatGridListModule, MatSelectModule, MatTabsModule,
    MatExpansionModule,


    FormsModule,

    SharedModule, MatIconButton, MatListModule
  ]
})
export class EventsManagementModule { }
