import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewTeamEntryComponent } from './new-team-entry.component';

describe('NewTeamEntryComponent', () => {
  let component: NewTeamEntryComponent;
  let fixture: ComponentFixture<NewTeamEntryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NewTeamEntryComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewTeamEntryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
