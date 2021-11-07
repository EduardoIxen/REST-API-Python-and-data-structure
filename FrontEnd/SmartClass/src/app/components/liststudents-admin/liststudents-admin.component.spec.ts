import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListstudentsAdminComponent } from './liststudents-admin.component';

describe('ListstudentsAdminComponent', () => {
  let component: ListstudentsAdminComponent;
  let fixture: ComponentFixture<ListstudentsAdminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListstudentsAdminComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListstudentsAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
