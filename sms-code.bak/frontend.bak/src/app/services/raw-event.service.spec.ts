import { TestBed } from '@angular/core/testing';

import { RawEventService } from './raw-event.service';

describe('RawEventService', () => {
  let service: RawEventService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RawEventService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
