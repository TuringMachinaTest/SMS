import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedComponent } from './shared.component';
import { RouterModule } from '@angular/router';
import { ConfirmationComponent } from './confirmation/confirmation.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,

    MatDialogModule, MatButtonModule
  ],
  declarations: [SharedComponent, ConfirmationComponent]
})
export class SharedModule { }
