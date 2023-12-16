my $input = <STDIN>;
my @words = split /,/, $input;
my $sum=0;
foreach $word ( @words ) {
  my $hash=0;
  foreach $char (split('', $word)) {
    $hash = (($hash + ord($char))*17) % 256;
  }
  $sum += $hash;
}
print "$sum";
