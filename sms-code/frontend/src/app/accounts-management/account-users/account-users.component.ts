import {AfterViewInit, Component, Input, OnInit, ViewChild} from '@angular/core';
import {Account} from "../../services/account.service";
import {map, startWith, switchMap} from "rxjs";
import {City, CityResponse, CityService} from "../../services/city.service";
import {MatTableDataSource} from "@angular/material/table";
import {CityComponent} from "../city/city.component";
import {ConfirmationComponent} from "../../shared/confirmation/confirmation.component";
import {MatPaginator} from "@angular/material/paginator";
import {MatDialog} from "@angular/material/dialog";

@Component({
  selector: 'app-account-users',
  templateUrl: './account-users.component.html',
  styleUrl: './account-users.component.css'
})
export class AccountUsersComponent implements OnInit, AfterViewInit {
  @Input()
  account: any = {} as Account;

  @Input()
  isView: boolean = false;

  displayedColumns: string[] = ['city', 'actions']

  dataSource = new MatTableDataSource<City>();

  @ViewChild(MatPaginator) paginator: any = MatPaginator;

  response: CityResponse | undefined

  pageSizes = [10];
  page = 1
  pageEvent: any | undefined
  isLoading = true

  constructor(private service: CityService, public dialog: MatDialog) {
  }

  ngOnInit() {

  }

  ngAfterViewInit() {

    this.getAll()

  }

  getAll(): void {
    this.paginator.page
      .pipe(
        startWith({}),
        switchMap(() => {
          this.isLoading = true
          return this.service.getAll$(
            this.paginator.pageIndex + 1,
          )
        }),
        map((models: CityResponse) => {
          if (models == null) return [];
          this.paginator.length = models.count
          return models.results;
        })
      )
      .subscribe((models: City[]) => {
        this.dataSource = new MatTableDataSource(models);
        this.isLoading = false
      });
  }

  view(model: City): void {
    const dialogRef = this.dialog.open(CityComponent, {
      data: {model, isView: true},
    }).afterClosed().subscribe(() => {
      this.getAll()
    });
  }

  add(): void {
    const dialogRef = this.dialog.open(CityComponent, {
      data: {isView: false, isEdit: false},
    }).afterClosed().subscribe(() => {
      this.getAll()
    })
  }

  edit(model: City): void {
    const dialogRef = this.dialog.open(CityComponent, {
      data: {model, isView: false, isEdit: true},
    }).afterClosed().subscribe(() => {
      this.getAll()
    });
  }

  delete(model: City): void {

    const dialogRef = this.dialog.open(ConfirmationComponent, {}).afterClosed().subscribe((res) => {
      if (res) {
        this.service.delete$(model).subscribe({
          next: any => {
            this.getAll()
          }
        })
      }
    });
  }
}
