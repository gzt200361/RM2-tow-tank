# Test sequence

1. Shakedown runs
  - [x] Find `tsr_max`
  - [x] Find `tsr_0` (where `cp` is maximum)
  - [x] Find max tow speed, or do a quick check for Re-independence
2. Settling runs: One for each tow speed we plan to use, with
   `tsr = tsr_0`
  - [x] Generate `Config/settling_times.csv`
3. Performance curves
  - [x] 4--6 performance curves--one or two above `Re_0`
  - [x] Some runs at in-between tow speeds at `tsr_0`
  - [x] Performance curve at `Re_0`
  - [x] Check for Re-independence by generating figure
4. Wake characteristics
  - [x] 4--6 cross-stream profiles at Re-independent tow speed, `tsr_0`
5. Strut torque runs
  - [ ] Remove blades
  - [ ] Measure strut torque at RPMs corresponding to the Re-independent
        performance curve
6. Strut torque with covers
  - [ ] Install strut covers and endcaps
  - [ ] Repeat measuring strut torque at RPMs corresponding to 
        Re-independent performance curve
7. Performance curve with strut covers
  - [ ] Install blades with strut covers
  - [ ] Repeat `Re_0` perf curve with strut covers
8. Tare torque
  - [ ] Calculate RPM range used throughout the experiment
  - [ ] Finalize test matrix
  - [ ] Remove blades, struts, hub sections
  - [ ] Do measurements in air
  - [ ] Update processing code to use this processed data
9. Tare drag
  - [ ] One tow at each speed used during the experiment
  - [ ] Update processing code to use this data
