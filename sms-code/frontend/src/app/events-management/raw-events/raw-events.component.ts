import {AfterViewInit, Component, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {MatTableDataSource} from "@angular/material/table";
import {MatPaginator} from "@angular/material/paginator";
import {MatDialog} from "@angular/material/dialog";
import {map, startWith, switchMap} from "rxjs";
import {RawEvent, RawEventResponse, RawEventService} from "../../services/raw-event.service";

@Component({
  selector: 'app-raw-events',
  templateUrl: './raw-events.component.html',
  styleUrl: './raw-events.component.css'
})
export class RawEventsComponent implements OnInit, AfterViewInit, OnDestroy{

  intervalId: any;

  displayedColumns: string[] = ['id', 'data', 'created_at', 'device_name']

  dataSource = new MatTableDataSource<RawEvent>();

  @ViewChild(MatPaginator) paginator :any = MatPaginator;

  response: RawEventResponse | undefined

  pageSizes = [10];
  page = 1
  pageEvent : any | undefined
  isLoading = true
  constructor(private service: RawEventService, public dialog: MatDialog) { }

  ngOnInit() {

    this.intervalId = setInterval(() => {
      this.getAll();
    }, 1000);
  }

  ngAfterViewInit() {

    this.dataSource.paginator = this.paginator;

    this.getAll()

  }

  ngOnDestroy() {
    clearInterval(this.intervalId);
  }

  getAll(): any {
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
      map((models: RawEventResponse) => {
        if (models == null) return [];
        this.paginator.length = models.count
        return models.results;
      })
    )
    .subscribe((models: RawEvent[]) => {
      this.dataSource = new MatTableDataSource(models);
      this.isLoading = false
    });
  }
}
