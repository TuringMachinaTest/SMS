import { ChangeDetectorRef, Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { City, CityService } from 'src/app/services/city.service';

@Component({
  selector: 'app-city',
  templateUrl: './city.component.html',
  styleUrls: ['./city.component.css']
})
export class CityComponent implements OnInit {

  model: City =  {} as City
  errorMessage = ""

  constructor(private service: CityService, public dialogRef: MatDialogRef<CityComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any, private cdref: ChangeDetectorRef ) { }
  ngOnInit() {
  }

  ngAfterViewInit(){
    if(this.data && this.data.model)
      this.model = this.data.model
    //console.log(this.data.name)
    this.cdref.detectChanges();

  }

  add() {
    if(this.data.isview)
    {
      return
    }

    this.service.add$(this.model).subscribe({
      next: account => {
        //this.account = account
        this.dialogRef.close()
    },
    error: error => {
      this.errorMessage = error.message;
      console.error('There was an error!', error);
    }

    })
  }

  edit(){

    if(this.data.isview)
    {
      return
    }

    this.service.edit$(this.model).subscribe({
      next: account => {
          //this.account = account
          this.dialogRef.close()
      },
      error: error => {
        this.errorMessage = error.message;
        console.error('There was an error!', error);
      }

    })
  }


}
