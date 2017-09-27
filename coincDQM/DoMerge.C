#include <TGrid.h>

void DoMerge(char* nomelista="lista",char* output="coincCERN_0102t.root"){

  FILE *f = fopen(nomelista,"r");

  TFileMerger m(kFALSE);
  m.OutputFile(output);

  Int_t i=0;
  char nome[100];
  while (fscanf(f,"%s",nome)==1) {
    m.AddFile(nome);
    i++;
  }
  if (i)
    m.Merge();
}

