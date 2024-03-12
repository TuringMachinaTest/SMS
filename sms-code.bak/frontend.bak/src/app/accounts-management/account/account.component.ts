import { ChangeDetectorRef, Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Account, AccountService } from 'src/app/services/account.service';
import { City, CityResponse, CityService } from 'src/app/services/city.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {

  model: any =  {} as Account
  cities: City[] = [] as City[]
  errorMessage = ""

  constructor(private service: AccountService, private cityService: CityService, public dialogRef: MatDialogRef<AccountComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any, private cdref: ChangeDetectorRef ) { }
  ngOnInit() {

  }

  ngAfterViewInit(){
    if(this.data && this.data.model)
      this.model = this.data.model
    console.log(this.data.model)
    this.cdref.detectChanges();

    this.cityService.getAll$(1).subscribe( (data: CityResponse) =>
    {
      this.cities = data.results
    })
  }

  add() {
    if(this.data.isview)
    {
      return
    }

    this.service.add$(this.model).subscribe({
      next: model => {
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
      next: model => {
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
