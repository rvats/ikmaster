using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Fairway.Controllers
{
    public class BorrowerRepository : IBorrowerRepository
    {
        public Task GetBorrowerTransactionsAsync(List<int> borrowerIds, string dateTime1, string dateTime2)
        {
            throw new NotImplementedException();
        }
    }
}