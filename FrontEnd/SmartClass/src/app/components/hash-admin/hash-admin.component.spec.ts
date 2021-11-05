import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HashAdminComponent } from './hash-admin.component';

describe('HashAdminComponent', () => {
  let component: HashAdminComponent;
  let fixture: ComponentFixture<HashAdminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HashAdminComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HashAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
