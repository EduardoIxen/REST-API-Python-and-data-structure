import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PensumAdminComponent } from './pensum-admin.component';

describe('PensumAdminComponent', () => {
  let component: PensumAdminComponent;
  let fixture: ComponentFixture<PensumAdminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PensumAdminComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PensumAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
