import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {RawEventsComponent} from "./raw-events/raw-events.component";
import {EventsManagementModule} from "./events-management.module";
import {
  MatCell,
  MatCellDef,
  MatColumnDef,
  MatHeaderCell, MatHeaderCellDef,
  MatHeaderRow,
  MatHeaderRowDef,
  MatRow, MatRowDef, MatTable
} from "@angular/material/table";
import {MatIcon} from "@angular/material/icon";
import {MatIconButton} from "@angular/material/button";
import {MatPaginator} from "@angular/material/paginator";
import {MatProgressBar} from "@angular/material/progress-bar";
import {NgIf} from "@angular/common";


const routes: Routes = [
  {path: "raw-events" , component: RawEventsComponent},
]


@NgModule({
  imports: [RouterModule.forChild(routes), MatCell, MatCellDef, MatColumnDef, MatHeaderCell, MatHeaderRow, MatHeaderRowDef, MatIcon, MatIconButton, MatPaginator, MatProgressBar, MatRow, MatRowDef, MatTable, NgIf, MatHeaderCellDef],
  exports: [RouterModule],
  declarations: [RawEventsComponent]
})
export class EventsManagementRoutingModule { }
