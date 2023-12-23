///load_jms(fname) -- loads jms map.
fname = argument0
i = 0;
fopen = file_text_open_read(fname)
      while !file_text_eof(fopen) {
      line[i] = file_text_read_string(fopen);
      file_text_readln(fopen)
      i+=1
      }
var xx, yy;
xx = -32; yy = 0;
            
for (m = 0 ; m<i ; m+=1 ) { // outler loop trough lines
    for (j = 0; j<=string_length(line[m]); j+=1 ) { // inner loop trough strings in line
        sdm(line[m])
        jms_eval_obj(string_char_at(line[m],j),xx,yy) {                
        }
        xx += 32;   
    }
    yy += 32;
    xx = -32;
}
