import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { catchError, map, startWith, switchMap } from 'rxjs';
import { AccountService, Account, AccountResponse } from 'src/app/services/account.service';
import { AccountComponent } from '../account/account.component';
import { ConfirmationComponent } from 'src/app/shared/confirmation/confirmation.component';
import {AuthService} from "../../services/auth.service";


@Component({
  selector: 'app-accounts',
  templateUrl: './accounts.component.html',
  styleUrls: ['./accounts.component.css'],
})

export class AccountsComponent implements OnInit {

  displayedColumns: string[] = ['account_number', 'name', 'city_name', 'security_number', 'memo' , 'actions']

  dataSource = new MatTableDataSource<Account>();

  @ViewChild(MatPaginator) paginator :any = MatPaginator;

  response: Response | undefined

  pageSizes = [10];
  page = 1
  pageEvent : any | undefined
  isLoading = true

  constructor(private service: AccountService, public dialog: MatDialog, private authService: AuthService) { }

  ngOnInit() {
  }

  ngAfterViewInit() {

    this.dataSource.paginator = this.paginator;

    this.getAll()

  }

  getAll(): void {
    this.paginator.page
    .pipe(
      startWith({
      }),
      switchMap(() => {
        this.isLoading = true
        return this.service.getAll$(
          this.paginator.pageIndex + 1,
        )
      }),
      map((models: AccountResponse) => {
        if (models == null) return [];
        this.paginator.length = models.count
        return models.results;
      })
    )
    .subscribe((models: Account[]) => {
      this.dataSource = new MatTableDataSource(models);
      this.isLoading = false
    });
  }

  view(model: Account): void{
    const dialogRef = this.dialog.open(AccountComponent, {
      data: {model, isView: true},
    }).afterClosed().subscribe(()=> {
      this.getAll()
    });
  }

  add(): void {
    const dialogRef = this.dialog.open(AccountComponent, {
      data: {isView: false, isEdit: false},
      width: '800px',
    }).afterClosed().subscribe(()=> {
      this.getAll()
    })
  }

  edit(model: Account): void {
    const dialogRef = this.dialog.open(AccountComponent, {
      data: {model, isView: false, isEdit: true},
    }).afterClosed().subscribe(()=> {
      this.getAll()
    });
  }

  delete(model: Account): void {

    const dialogRef = this.dialog.open(ConfirmationComponent, {
    }).afterClosed().subscribe((res) => {
      if(res)
      {
        this.service.delete$(model).subscribe({
          next: any => {
            this.getAll()
          }
        })
      }
    });


  }
}
