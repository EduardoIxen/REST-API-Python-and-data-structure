import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchcourseStudentComponent } from './searchcourse-student.component';

describe('SearchcourseStudentComponent', () => {
  let component: SearchcourseStudentComponent;
  let fixture: ComponentFixture<SearchcourseStudentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchcourseStudentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchcourseStudentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
