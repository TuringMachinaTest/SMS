import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RawEventsComponent } from './raw-events.component';

describe('RawEventsComponent', () => {
  let component: RawEventsComponent;
  let fixture: ComponentFixture<RawEventsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RawEventsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RawEventsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
