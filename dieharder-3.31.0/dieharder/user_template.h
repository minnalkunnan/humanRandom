/*
 * This is an example header file for a test.  For existing tests these
 * headers are in the library includes already, but this one is an example
 * suitable for use as a template.
 */

/*
 * The function needs a prototype.  In order to use the standard test
 * creation/destruction/execution routines, the prototype should have
 * precisely this form.
 */
int user_template(Test **test,int irun);

/*
 * This is default data for the test at hand.  The first field is
 * the test name.  The second is the test description.  The third
 * is the default number of p-values generated by a run for display
 * in a histogram and to generate a cumulative test p-value using
 * Kuiper-Kolmogorov-Smirnov.  The fourth is the number of "samples"
 * accumulated per test, if relevant (some tests do not permit this
 * to be varied).  The fifth and final Dtest parameter is the number
 * of statistics generated by the test (per test invocation) -- usually
 * this will be one but for several it is two and could be more.
 */
static Dtest user_template_dtest = {
  "Example User Test",
  "user_template",
  "\n\
#==================================================================\n\
#                  Example Dieharder Test\n\
#\n\
#                     Lagged Sum Test\n\
# This package contains many very lovely tests.  Very few of them,\n\
# however, test for lagged correlations -- the possibility that\n\
# the random number generator has a bitlevel correlation after\n\
# some period.  Diehard tests, for example, COULD NOT test for this\n\
# sort of thing with only a few million rands to sample from.\n\
# The template test is therefore very simple.  It takes a user-\n\
# specified lag (-x lag) and adds up uniform deviates sampled with\n\
# that lag.  The mean of tsamples samples summed should be\n\
# 0.5*tsamples.  The standard deviation should be sqrt(tsamples/12).\n\
# The experimental values of the sum are thus converted into a\n\
# p-value (using the erf()) and a ks-test applied to psamples of them.\n\
#==================================================================\n",
  100,
  100000,
  1,
  user_template,
  0
};

