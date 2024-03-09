import {AfterViewInit, Component, OnInit, ViewChild} from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { map, startWith, switchMap } from 'rxjs';
import { City, CityResponse, CityService } from 'src/app/services/city.service';
import { CityComponent } from '../city/city.component';
import { ConfirmationComponent } from 'src/app/shared/confirmation/confirmation.component';

@Component({
  selector: 'app-cities',
  templateUrl: './cities.component.html',
  styleUrls: ['./cities.component.css']
})
export class CitiesComponent implements OnInit, AfterViewInit {

  displayedColumns: string[] = ['city', 'actions']

  dataSource = new MatTableDataSource<City>();

  @ViewChild(MatPaginator) paginator :any = MatPaginator;

  response: CityResponse | undefined

  pageSizes = [10];
  page = 1
  pageEvent : any | undefined
  isLoading = true

  constructor(private service: CityService, public dialog: MatDialog) { }

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

  view(model: City): void{
    const dialogRef = this.dialog.open(CityComponent, {
      data: {model, isView: true},
    }).afterClosed().subscribe(()=> {
      this.getAll()
    });
  }

  add(): void {
    const dialogRef = this.dialog.open(CityComponent, {
      data: {isView: false, isEdit: false},
    }).afterClosed().subscribe(()=> {
      this.getAll()
    })
  }

  edit(model: City): void {
    const dialogRef = this.dialog.open(CityComponent, {
      data: {model, isView: false, isEdit: true},
    }).afterClosed().subscribe(()=> {
      this.getAll()
    });
  }

  delete(model: City): void {

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
